import com.evernote.auth.EvernoteAuth;
import com.evernote.auth.EvernoteService;
import com.evernote.clients.ClientFactory;
import com.evernote.clients.NoteStoreClient;
import com.evernote.edam.error.EDAMSystemException;
import com.evernote.edam.error.EDAMUserException;
import com.evernote.edam.type.Notebook;
import com.evernote.thrift.TException;

import java.util.List;

public class Main {
    public static void main(String[] args) throws TException, EDAMUserException, EDAMSystemException {
        var auth = new EvernoteAuth(EvernoteService.SANDBOX, "TODO");
        ClientFactory factory = new ClientFactory(auth);
        NoteStoreClient noteStoreClient = factory.createNoteStoreClient();

        List<Notebook> notebooks = noteStoreClient.listNotebooks();
        for(var notebook : notebooks)
        {
            System.out.println(notebook);
        }
    }
}
