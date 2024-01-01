from django.contrib.auth import get_user_model


def reset_password(email, password):
    try:
        user = get_user_model().objects.get(email=email)
    except Exception as err:
        return "User could not be found " + str(err)
    user.set_password(password)
    user.save()
    return "Password has been changed successfully"
