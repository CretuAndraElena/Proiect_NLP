from translate import Translator
translator= Translator(to_lang="ro")
translation = translator.translate("This is a pen.")
print(translation)