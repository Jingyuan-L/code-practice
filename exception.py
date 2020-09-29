def div(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Error: b should not be 0!")
    except Exception as e:
        print("Unexpected Error: {}".format(e))
    else:
        print("Everything goes well!")
    finally:
        print("Always run this block")

div(2, 0)
div(2, "bad type")
div(1, 2)