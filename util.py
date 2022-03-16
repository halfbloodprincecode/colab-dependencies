def Drive():
  from google.colab import drive
  drive.mount('/content/drive')
  drive.flush_and_unmount()
  drive.mount('/content/drive')