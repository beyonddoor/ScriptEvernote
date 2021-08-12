from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

tagNameSet = set()

DEV_TOKEN = ''
with open('keys/token.txt', 'r') as file:
    DEV_TOKEN = file.read()

def tryCreateTag(noteStore, tagName):
    if tagName in tagNameSet:
        return
    tag = Types.Tag(name=tagName)
    noteStore.createTag(DEV_TOKEN, tag)

def createDayTags(noteStore):
    for month in range(1, 13):
        for day in range(1, 32):
            tryCreateTag(noteStore, 'd{:02d}{:02d}'.format(month, day))


def createMonthTags(noteStore, fromYear, toYear):
    for year in range(fromYear, toYear+1):
        for month in range(1, 13):
            tryCreateTag(noteStore, 'm{}{:02d}'.format(year, month))
 
client = EvernoteClient(token=DEV_TOKEN, sandbox=True, china=False)
noteStore = client.get_note_store()

notebooks = noteStore.listNotebooks()
for notebook in notebooks:
    print "Notebook: ", notebook.name

tags = noteStore.listTags()
for tag in tags:
    tagNameSet.add(tag.name)

createMonthTags(noteStore, 2020, 2021)
createDayTags(noteStore)

userStore = client.get_user_store()
user = userStore.getUser()
print(user.username)