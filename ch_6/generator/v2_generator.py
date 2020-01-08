

def myxml(default, content="", **kwargs):

    k_w_args = "".join([f" {key}={value}" for key, value in kwargs.items()])
    return f"<{default}{k_w_args}>{content}</{default}>"
print(myxml('foo', 'bar', a=1, b=2, c=3))
