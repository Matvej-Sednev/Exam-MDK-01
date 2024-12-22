package com.example.lab_05;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity2 extends AppCompatActivity {

    EditText txt2;
    Button ok, no;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        txt2 = findViewById(R.id.txt2);

        Intent i = getIntent();

        String s = i.getStringExtra("abc");
        txt2.setText(s);
    }

    private void no(View view){
        setResult(RESULT_CANCELED);
        finish();
    }

    private void ok(View view){
        Intent i = new Intent();

        String s = txt2.getText().toString();
        i.putExtra("qwe", s);

        setResult(RESULT_OK, i);
        finish();
    }
}