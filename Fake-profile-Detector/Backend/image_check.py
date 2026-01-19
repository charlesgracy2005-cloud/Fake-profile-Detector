"""
image_check.py
Performs a basic reverse image suspicion check (educational placeholder)
"""

def reverse_image_check(image_url):
    """
    Simulates reverse image search result.
    """

    result = {
        "image_suspicious": False,
        "reason": ""
    }

    if "default" in image_url.lower() or "avatar" in image_url.lower():
        result["image_suspicious"] = True
        result["reason"] = "Default or stock profile image detected"

    return result
