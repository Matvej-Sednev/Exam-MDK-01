package com.example.lab_06;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;

public class MainActivity extends AppCompatActivity {



    ArrayAdapter <nnote> adp;
    int sel;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        adp = new ArrayAdapter <nnote> (this, android.R.layout.simple_list_item_1);

        ListView lst = findViewById(R.id.bt_notes);
        lst.setAdapter(adp);

        lst.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                sel=position;
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @NonNull Intent data){
        if (data != null){
            int pos = data.getIntExtra("my-note-index", 1);
            String title = data.getStringExtra("my-note-title");
            String content = data.getStringExtra("my-note-content");

            nnote n = adp.getItem(pos);
            n.title = title;
            n.content = content;

            adp.notifyDataSetChanged();

        }
        super.onActivityResult(requestCode,resultCode,data);
    }


    public void new_click(View view) {
        nnote n = new nnote();
        n.title = "New note";
        n.content = "Some content";

        adp.add(n);
        int pos = adp.getPosition(n);

        Intent i = new Intent(this, MainActivity2.class);
        i.putExtra("my-note-index", pos);
        i.putExtra("my-note-title", n.title);
        i.putExtra("my-note-content",n.content);

        startActivityForResult(i, 12345);
    }

    public void edit_click(View view) {
        if (sel != -1) {
            nnote selectedNote = adp.getItem(sel);

            Intent i = new Intent(this, MainActivity2.class);
            i.putExtra("my-note-index", sel);
            i.putExtra("my-note-title", selectedNote.title);
            i.putExtra("my-note-content", selectedNote.content);

            startActivityForResult(i, 12345);
        }
    }

    public void delete_click(View view) {
        if (sel != -1) {
            adp.remove(adp.getItem(sel));
            adp.notifyDataSetChanged();
        }
    }
}
//Голодникова Валерия 225 группа