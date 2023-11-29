from django.shortcuts import render,HttpResponse
from googletrans import Translator
# Create your views here.
word_list=[]
def translater(request):
    if request.method == "GET":
        return render(request,"index.html")
    elif request.method == "POST":
        def translate_text(text, target_language='ta'):  # 'ta' is the language code for Tamil
            translator = Translator()
            translation = translator.translate(text, dest=target_language)
            return translation.text

        # Example usage
        english_text = request.POST.get("word_name")
        tamil_translation = translate_text(english_text)
        # print(f"English: {english_text}")
        # print(f"Tamil: {tamil_translation}")

            # return HttpResponse("hallo world")
            # get_word = request.POST.get("word_name")
        word_list.append(tamil_translation)
        # print(word_list)
        return render(request,"index.html",{"values":word_list})


