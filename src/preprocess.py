import re
import emoji
import langid

def preprocess_text(text, targets):

    # First Demojize Text
    edited_text = emoji.replace_emoji(text, '')

    # Mask company
    try:
        pattern = r'(?<![a-zA-Z])(?:' + '|'.join(re.escape(word) for word in targets if isinstance(word, str)) + r')(?![a-zA-Z])'
        if re.search(pattern, text, flags=re.IGNORECASE):
            edited_text = re.sub(pattern, "TargetedCompany", text, flags=re.IGNORECASE)
        else:
            edited_text = ""

    except Exception as e:
        raise

    # lower case
    edited_text = edited_text.lower()

    # remove links, mentions, hashtags
    edited_text = re.sub(r"http\S+|www\S+|@\w+|#\w+", '', edited_text)

    # Remove numbers
    edited_text = re.sub(r'\d+', '', edited_text)

    # Remove non ASCII
    edited_text = re.sub(r'[^\x00-\x7F]+', '', edited_text)

    # remove extra spaces
    edited_text = re.sub(r'\s+', ' ', edited_text).strip()

    # return if text is empty
    if edited_text == "":
        return edited_text

    # Remove non english
    try:
        # lang = detect(edited_text)
        lang, _ = langid.classify(edited_text)
        if lang != "en":
            edited_text = ""
    except Exception as e:
        # print(f"Error detecting language for text at index {index} and content:{edited_text}: {e}")
        edited_text = ""

    return edited_text

if __name__ == "__main__":
    result = preprocess_text("Hello this is a test of http://www.google.com 859", targets=['this'])
    print(result)
