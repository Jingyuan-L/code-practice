def user_info(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "admin":
                print("admin %s" % func.__name__)
            elif level == "customer":
                print("customer %s" % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@user_info(level="admin")
def user(name="Jillian"):
    print("user %s" % name)


user()
