class bigjpg:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "int_field": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": 4096, #Maximum value
                    "step": 64, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "float_field": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001, #The value represeting the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display": "number"}),
                "print_to_screen": (["enable", "disable"],),
                "string_field": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Hello World!"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "bigjpg"

    def test(self, image, string_field, int_field, float_field, print_to_screen):
        return (image,)

    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique  注意:名称应该是全局唯一的
NODE_CLASS_MAPPINGS = {
    "bigjpg": bigjpg  # 将节点名称与节点类进行映射。在这个示例中，将节点名称"Example"与类Example进行映射。
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "bigjpg": "bigjpg Node"  # 节点名称与友好/可读的节点标题进行映射。在这个示例中，将节点名称"Example"与节点标题"Example Node"进行映射。
}

