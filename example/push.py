from pushingbox import PushingBox

def main():
    key = "v1234567890ABCDEF"  # change to your key
    pb = PushingBox(key, room="attic")  # push notification for attic...
    err = pb.push(temp=100)  # ... that temperature reached 100F
    if err != "":
        print("Error: ", err)

if __name__ == "__main__": main()