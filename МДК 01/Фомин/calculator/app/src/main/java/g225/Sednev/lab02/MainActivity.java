package g225.Sednev.lab02;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    @SuppressLint("SetTextI18n")
    public void do_stuff(View v)
    {
        EditText ta = findViewById(R.id.input_a);
        EditText tb = findViewById(R.id.b_num);
        TextView tr = findViewById(R.id.res_num);

        Button bplus = findViewById(R.id.but_plus);
        Button bminus = findViewById(R.id.but_min);
        Button bmul = findViewById(R.id.but_umn);
        Button bcos = findViewById(R.id.but_cos);
        Button bsin = findViewById(R.id.but_sin);
        Button btg = findViewById(R.id.but_tan);
        Button bsqrt = findViewById(R.id.but_sqrt);
        Button bpow = findViewById(R.id.but_pow);
        Button bdiv = findViewById(R.id.but_del);
        RadioButton brad = findViewById(R.id.per_rad);
        RadioButton bgrad = findViewById(R.id.per_grad);

        String sa = ta.getText().toString();
        String sb = tb.getText().toString();
        double a = 0, b = 0;

        try {
            a = Double.parseDouble(sa);
            b = Double.parseDouble(sb);
        }
        catch (Exception e1)
        {
            tr.setText("One or booth values are empty");
            return;
        }


        double r = 0;

        if (v == bplus)  r = a + b;
        if (v == bminus) r = a - b;
        if (v == bmul) r = a * b;
        if (v == bdiv)
        {
            if (b == 0)
            {
                tr.setText("Do not divide by zero");
                return;
            }
            r = a / b;
        }
        if (v == bpow) r = Math.pow(a, b);
        if (v == bsin) {r = Math.sin(a);}
        if (v == bcos) r = Math.cos(a);
        if (v == bsqrt)
        {
            r = Math.sqrt(a);
        }
        if (v == btg) {
            if (a == 270 || a == 90){
                tr.setText("Error 90 or 270 tangens no work");
                return;
            }
            else {
            r = Math.tan(a);}}
        tr.setText(String.valueOf(r));
    }
}