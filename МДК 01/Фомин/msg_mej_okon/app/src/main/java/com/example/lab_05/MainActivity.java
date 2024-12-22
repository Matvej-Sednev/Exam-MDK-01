package com.example.lab_05;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    EditText txt1;
    Button open, close;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txt1 = findViewById(R.id.txt1);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @NonNull Intent data){
        if(requestCode == 555){
            if (data != null){
                String s = data.getStringExtra("qwe");
                Toast.makeText(this, s, Toast.LENGTH_SHORT).show();
            }
        }
        super.onActivityResult(requestCode, resultCode, data);
    }
    public void close(View view){
        finish();

    }

    public void open(View view){
        String s = txt1.getText().toString();

        Intent i = new Intent(this, MainActivity2.class);
        i.putExtra("abc",s);

        startActivityForResult(i, 555);
    }


}