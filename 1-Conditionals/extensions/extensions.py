name = input("What is the name of the file?")
if name.endswith("gif"):
    print("image/gif")
elif name.endswith("jpg"):
    print("image/jpeg")
elif name.endswith("png"):
    print("image/png")
elif name.endswith("pdf"):
    print("application/pdf")
elif name.endswith("txt"):
    print("application/txt")
elif name.endswith("zip"):
    print("application/zip")
else:
    print("application/octect-stream")
