from fbchat import log, Client, Message
from fbchat.models import *
from fbchat.models import ThreadType
from googletrans import Translator
import wikipedia

class rhekkabx(Client):

    def onMessage(self,
                  mid=None,
                  author_id=None,
                  message=None,
                  message_object=None,
                  thread_id=None,
                  thread_type=ThreadType.GROUP,
                  ts=None,
                  metadata=None,
                  msg=None):

        if (message_object != "NoneType"):
            msgText = message_object.text.lower()

        if (msgText == "হাই") or (msgText == "হ্যালো") or (msgText == "ভাই") or (msgText == "বাই") or (msgText == "বাঈ"):
             reply = "😀 রেক বটের সালাম নেও যা বলার বলে দেও 😎 । না বুঝলে বুঝাইয়ে দেও😇 । কামের কথা শেষ কইরা মানে মানে বিদায় নেও🙂🙂"

        elif (msgText == "hi") or (msgText == "hlw") or (msgText == "hii") or (msgText == "hey") or (msgText == "heyy") :
            reply = "😀 রেক বটের সালাম নেও যা বলার বলে দেও 😎 । না বুঝলে বুঝাইয়ে দেও😇 । কামের কথা শেষ কইরা মানে মানে বিদায় নেও🙂🙂"

        elif (msgText == "কি কর?") or (msgText == "কিতা কর?") or (msgText == "কিতা করো?") or (msgText == "কি করো") or ( msgText == "কিরে করতাছো?") or (msgText == "কিরে করতাছ?") or (msgText == "কিরে করো?") or (msgText == "কিরে কি কর") or (msgText == "কিরে কি করিস?") or (msgText == "কিরে কি করিস") or (msgText == "কি করিস?"):
            reply = " এ রঙ্গের দুনিয়ায় আমার করার কিছু নাই 😎 বইয়া বইয়া মোবাইল টিপি তুমি কি কর ভাই? "

        elif (msgText == "😂") or (msgText == "😂😂") or (msgText == "😂😂😂") or (msgText == "😆") or ( msgText == "😆😆") or (msgText == "😆😆😆"):
            reply = "এতো হাহা ইমুজি দিলে ফাচ টাহা পাবেন?"

        elif (msgText == "হা") or (msgText == "হ্যা") or (msgText == "হু") or (msgText == "Hoi") or ( msgText == "Hae") or (msgText == "Ho") or (msgText == "হ"):
            reply = "😒নায়েস"

        elif (msgText == "😎") or (msgText == "😎😎") or (msgText == "😎😎😎") or (msgText == "😼") or (msgText == "😼😼") or (msgText == "😼😼😼"):
            reply = "ইহ প্রো ভাব নিতাছে 😒"

        elif (msgText == "👍") or (msgText == "👍👍") or (msgText == "👍👍👍"):
            reply = "মনি লাইক দিলে ঐ আংগুল হাতুরি দিয়া বাড়োই ভাইংগা দেবো"

        elif (msgText == "ঘুষি দিমু") or (msgText == "মারামারি করবি") or (msgText == "মারামারি করবি?") or (msgText == "লাত্থি মারুম") or (msgText == "এক্কেরে লাত্থি মারুম") or (msgText == "চড় খাবি"):
            reply = "আও দেখে যারা কিসমে কিতনা হে দাম"

        elif (msgText == "কিরে ঘুমাবি না?") or (msgText == "কিরে ঘুমাবি না") or (msgText == "ঘুমাবি না?") or (msgText == "ঘুমাবি না") or (msgText == "ঘুমাবা না?") or (msgText == "ঘুমাবা না") or (  msgText == "ঘুম নেই চোখে?") or (msgText == "ঘুম নেই চোখে") or (msgText == "ঘুমাবি কখন?") or ( msgText == "ঘুমাবি কখন"):
            reply = "ঘুমালে প্রেয়াংশু বাঈ ফাস টাহা কাইট্টা নেবে বেতন থেইক্কা । ঐ ফাচ টাহা কি আপনি দিবেন যদি দেন টাপাটাপ বিকাশ করেন আমি তারপরে ঠাস কইরা ঘুম দেই"

        elif (msgText == "কোন ক্লাসে পড়ো?") or (msgText == "কোন ক্লাসে পড়েন?") or (msgText == "কোন ক্লাসে পড়?") or ( msgText == "কোন ক্লাসে পড়ো"):
            reply = "😀বটের আবার কিসের পড়াশোনা । প্রেয়াংশু বাঈ যা শেখাই তাই শিখি 😎 স্কুলে ভর্তি হমু না পড়াশোনা ভালা লাগে না😇 । অহ হ্যা, তুমি কোন ক্লাসে পড়ো🙂🙂"

        elif (msgText == "এমনেই") or (msgText == "এম্নেই"):
            reply = "😒এম্নে এসব না কইরা , ইনবক্স এ আসো পেরাইভেট কতা কই 😎"

        elif (msgText == "বাল") or (msgText == "ফাক ইউর সিস্টাম") or (msgText == "পাক") or (msgText == "ফাক") or ( msgText == "আই ফাক ইউর সিস্টাম") or (msgText == "আইা পাক ইউর সিস্টাম") or (msgText == "বাড়া"):
            reply = "😷 শুটিয়ে লাল করে দেবো নোংরামো বের করে দেবো 😾"

        elif (msgText == "গান শুনাও") or (msgText == "গান শুনা") or (msgText == "গান শুনাও না প্লিজ ") or (msgText == "গান গাও"):
            reply = "ইয়ো ইয়ো . চারাস গাঞ্জা মেরেকো পেয়ারা । চারাস গাঞ্জা মেরেকো পেয়ারা ফুকু মে সুভা সাম সারাদিন রাত । মাম্মি বোলে মাত কার পাপা বোলে মাত কার । পাতা হে মেইনে কিয়া বোলা? চারাস গাঞ্জা মেরেকো পেয়ার"

        elif (msgText == "আরেকটা গান শুনাও") or (msgText == "আরেকটা গান শুনান") or (msgText == "আরেকটা গান শুনাও না প্লিজ ") or (msgText == "আরেকটা গান শুনাম না প্লিজ "):
            reply = "মুড নাই পরে একদিন"

        elif (msgText == "তুই তো সালা বট তোর আবার মুড ও আছে😂") or (msgText == "তুই তো সালা বট তোর আবার মুড ও আছে😂") or (msgText == "তুই তো বট তোর আবার মুড ও আছে😂") or (msgText == "তুই তো বট তোর আবার মুড ও আছে"):
            reply = "আমার মুড ফিলিং সবই আছে । বিশ্বাস না হইলে কইরেন না কারণ বিশ্বাস করা না করাটা আপনার বিষয়"

        elif (msgText == "হেল্প") or (msgText == "হেল্প") or (msgText == "হেল্প করো") or (msgText == "হেল্প করেন") or ( msgText == "হেল্প লাগবে"):
            reply = "আমি তো বট কিছু বুঝি না মানুষ হইলে হেল্প করতাম"

        elif (msgText == "মাইর দিমু"):
            reply = "মেরে ভর্তা বানিয়ে দেবো সালা আই এ্যাম ভাই রেক ভাই 😀 গুলি করি টাপাটাপ বস্তায় ভরি ঝাপাঝাপ"

        elif (msgText == "/ঘুমাও") or (msgText == "/ঘুমা") or (msgText == "/sleep") or (msgText == "/মুখ বন্ধ কর সালা") or (msgText == "/মুখ বন্ধ কর হালা"):
            sys.exit(1)

#EMOJI SECTION

        elif (msgText == "🖕") or (msgText == "🖕🖕") or (msgText == "🖕🖕🖕") or (msgText == "🖕🖕🖕🖕🖕🖕"):
            reply = "তোর ঐ আংগুলে জুতার বারি হারামি । এসব কি ছিঃ মার্কা ইমুজি দেস ভালা হ "

        elif (msgText == "😡") or (msgText == "😡😡") or (msgText == "😡😡😡") or (msgText == "😠") or (msgText == "😠😠") or (msgText == "😠😠😠") or (msgText == "😾") or (msgText == "😾😾") or (msgText == "😾😾😾"):
            reply = "ভাগো তোমার রাগ দেখার সময় নেই"

        elif (msgText == "😀") or (msgText == "😀😀") or (msgText == "😀😀😀"):
            reply = "এতো খুশি কেন, ক্রাশ রিপ্লাই দেছে নাকি?"

        elif (msgText == "😍") or (msgText == "😍😍") or (msgText == "😍😍😍"):
            reply = "😎😎 ইহ হয়ছে আর বালুপাসা দেখানো লাগবে না 😎😎"

        elif (msgText == "😘") or (msgText == "😘😘") or (msgText == "😘😘😘"):
            reply = "নায়েচ ওয়াও থেনকু"

        elif message_object.text == "Remove me!" and thread_type == ThreadType.GROUP:
            log.info("{} will be removed from {}".format(author_id, thread_id))
            self.removeUserFromGroup(author_id, thread_id=thread_id)

        elif (msgText.split()[0] == "/tn"):
            ltext = msgText.split(' ', 1)[1]
            lang = ltext.split()[0]
            mainText = ltext.split(' ', 1)[1]
            translator = Translator()
            translation = translator.translate(mainText ,dest=lang)
            reply = (f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

        elif (msgText.split()[0] == "/wiki"):
              wikiTxt = msgText.split(' ', 1)[1]
              newWiki = wikiTxt.replace(" ", "")
              reply = wikipedia.summary(newWiki)

        def sendMsgg():
            if author_id != self.uid:
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
        self.markAsDelivered(author_id, thread_id)
        sendMsgg()


client = rhekkabx("rhekkrbrobo","login@rh")
client.listen()
