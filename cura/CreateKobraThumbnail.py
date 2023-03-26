#------------------------------------------------------------------------------
# Cura JPEG Thumbnail creator
# Professional firmware for Ender3v2
# Miguel A. Risco-Castillo
# Modified Version for Kobra Max: Vasileios Antoniadis
# version: 1.4
# date: 2022-05-18
#
# Contains code from:
# https://github.com/Ultimaker/Cura/blob/master/plugins/PostProcessingPlugin/scripts/CreateThumbnail.py
#------------------------------------------------------------------------------
import binascii
import time  # add this import statement to use time.sleep()

from UM.Logger import Logger
from cura.Snapshot import Snapshot
from cura.CuraVersion import CuraVersion

from ..Script import Script


class CreateKobraThumbnail(Script):
    def __init__(self):
        super().__init__()

    def _createSnapshot(self):
        width = 150
        height = 120
        Logger.log("d", "Creating thumbnail image...")
        try:
            return Snapshot.snapshot(width, height)
        except Exception:
            Logger.logException("w", "Failed to create snapshot image")

    def _encodeSnapshot(self, snapshot, quality=50):      
        Major = 0
        Minor = 0
        try:
            Major = int(CuraVersion.split(".")[0])
            Minor = int(CuraVersion.split(".")[1])
        except:
            pass

        if Major < 5:
            from PyQt5.QtCore import QByteArray, QIODevice, QBuffer
        else:
            from PyQt6.QtCore import QByteArray, QIODevice, QBuffer

        Logger.log("d", "Encoding thumbnail image...")
        try:
            thumbnail_buffer = QBuffer()
            if Major < 5:
                thumbnail_buffer.open(QBuffer.ReadWrite)
            else:
                thumbnail_buffer.open(QBuffer.OpenModeFlag.ReadWrite)
            thumbnail_image = snapshot
            thumbnail_image.save(thumbnail_buffer, "JPG", quality=quality)  # pass quality argument
            hex_bytes = binascii.hexlify(thumbnail_buffer.data())
            hex_message = hex_bytes.decode('ascii')
            thumbnail_buffer.close()
            return hex_message
        except Exception:
            Logger.logException("w", "Failed to encode snapshot image")

    def _convertSnapshotToGcode(self, encoded_snapshot, chunk_size=480):
        gcode = []

        encoded_snapshot_length = len(encoded_snapshot)
        gcode.append(";")
        # compute the final size and length and add it to the gcode string
        additional_size = 12 * ((len(encoded_snapshot) // chunk_size)+1) + chunk_size - (len(encoded_snapshot) % chunk_size)
        final_size = encoded_snapshot_length + additional_size
        gcode.append("; thumbnail kobra 150x120 {}".format(final_size))

        address = 0x8000
        line_length = 78  # We subtract 2 to account for the semicolon and the newline character
        chunks = []
        current_line = "; "
        n_additions = 0  # count the number of times the "5AA5F3..." string is added
        for i in range(0, len(encoded_snapshot), chunk_size):
            chunk = encoded_snapshot[i:i+chunk_size]
            if len(chunk) < chunk_size:
                chunk += '0' * (chunk_size - len(chunk))
            chunk_comment = "5AA5F382{:04X}{}".format(address, chunk)
            n_additions += 1  # increment the count
            while len(chunk_comment) > 0:
                remaining_space = line_length - len(current_line)
                current_line += chunk_comment[:remaining_space]
                chunk_comment = chunk_comment[remaining_space:]
                if len(current_line) == line_length:
                    gcode.append(current_line)
                    current_line = "; "
            address += 0x78

        if len(current_line) < line_length and len(current_line) > 1:
            gcode.append(current_line)

        gcode.append("; thumbnail end")
        gcode.append(";")

        return gcode

    def getSettingDataString(self):
        return """{
            "name": "Create Kobra Thumbnail",
            "key": "CreateKobraThumbnail",
            "metadata": {},
            "version": 2,
            "settings": {}
        }"""


    def execute(self, data):
        snapshot = self._createSnapshot()
        if snapshot:
            quality = 50
            while True:
                encoded_snapshot = self._encodeSnapshot(snapshot, quality)
                snapshot_gcode = self._convertSnapshotToGcode(encoded_snapshot)
                final_size = len("\n".join(snapshot_gcode))
                if final_size < 6000:
                    break
                quality -= 3

            for layer in data:
                layer_index = data.index(layer)
                lines = data[layer_index].split("\n")
                for line in lines:
                    if line.startswith(";Generated with Cura"):
                        line_index = lines.index(line)
                        insert_index = line_index + 1
                        lines[insert_index:insert_index] = snapshot_gcode
                        break

                final_lines = "\n".join(lines)
                data[layer_index] = final_lines

        return data


