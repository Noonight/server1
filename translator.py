from google_trans_new import google_translator

translator = google_translator()

def detectLanguage(text):
    return {'lang':translator.detect(text)}

def translate(text, of, to):
    print(translator.translate(text, lang_tgt=to))
    if of is None:
        jsonResponse = {'fromText':text, 'text':translator.translate(text, lang_tgt=to).rstrip(), 'to':to}
        return jsonResponse
    else:
        jsonResponse = {'fromText':text, 'text':translator.translate(text, lang_src=of, lang_tgt=to).rstrip(), 'from':of, 'to':to}
        return jsonResponse