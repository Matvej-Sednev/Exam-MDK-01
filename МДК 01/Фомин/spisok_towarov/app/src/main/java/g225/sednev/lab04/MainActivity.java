package g225.sednev.lab04;

import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity
{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }

    CheckBox[] chk = new CheckBox[4];
    EditText[] num = new EditText[4];

    EditText[] val = new EditText[4];


    @SuppressLint("DefaultLocale")
    public  void  onCalc(View v)
    {


        chk[0] = findViewById(R.id.Apple);
        chk[1] = findViewById(R.id.Strawberry);
        chk[2] = findViewById(R.id.Bluberry);
        chk[3] = findViewById(R.id.Potatoes);


        num[0] = findViewById(R.id.AppleQuantity);
        num[1] = findViewById(R.id.StrawberryQuantity);
        num[2] = findViewById(R.id.BluberryQuantity);
        num[3] = findViewById(R.id.PotatoesQuantity);

        val[0] = findViewById(R.id.AppleValue);
        val[1] = findViewById(R.id.StrawberryValue);
        val[2] = findViewById(R.id.BluberryValue);
        val[3] = findViewById(R.id.PotatoesValue);

        RadioButton button1 = findViewById(R.id.Dialog);
        RadioButton button2 = findViewById(R.id.Toasts);

        String res = "";
        for (int i = 0; i < 4; i++)
        {
            if (num[i].getText().toString().equals("") || val[i].getText().toString().equals(""))
            {
                res = ("ERROR Empty Box('s)");
                Toast toast = Toast.makeText(getApplicationContext(), res, Toast.LENGTH_LONG);
                toast.setGravity(Gravity.CENTER, 0, 150);
                toast.show();
                return;
            }
        }

        int n = 4;
        boolean a = false;
        double itog = 0;

        for (int i = 0; i < n; i++)
        {
            if (num[i].getText().toString() == "" || val[i].getText().toString() ==  "")
            {
                res = ("Nothing Selected");
                Toast toast = Toast.makeText(getApplicationContext(), res, Toast.LENGTH_LONG);
                toast.setGravity(Gravity.CENTER, 0, 150);
                toast.show();
                break;
            }
            if (chk[i].isChecked()){
                double q = Double.parseDouble(num[i].getText().toString());
                double sum = q * Double.parseDouble(val[i].getText().toString());
                itog += sum;
                res += String.format("%d: %.2f x %s = %.2f x %.2f = %.2f\n", i, q, chk[i].getText().toString(), q, Double.parseDouble(val[i].getText().toString()), sum);
            }
        }

        if (button1.isChecked())
        {
            res += String.format("total - %.2f",itog);
            if (chk[0].isChecked() == a && chk[1].isChecked() == a && chk[2].isChecked() == a && chk[3].isChecked() == a)
            {
                res = ("Nothing Selected");
            }
            AlertDialog.Builder builder = new AlertDialog.Builder(this);
            builder.setMessage(res)
                    .setTitle("Dialog Title")
                    .setIcon(R.drawable.image)
                    .setPositiveButton("OK", new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int id) {
                            // User clicked OK button
                        }
                    });
            AlertDialog dialog = builder.create();
            dialog.show();
        }
        if (button2.isChecked())
        {
            res = "";
            if (chk[0].isChecked() == a && chk[1].isChecked() == a && chk[2].isChecked() == a && chk[3].isChecked() == a)
            {
                res = ("Nothing Selected");
                Toast toast = Toast.makeText(getApplicationContext(), res, Toast.LENGTH_LONG);
                toast.setGravity(Gravity.CENTER, 0, 150);
                toast.show();
            }
            else {
                res += String.format("total - %.2f",itog);
                Toast toast = Toast.makeText(getApplicationContext(), res, Toast.LENGTH_LONG);
                toast.setGravity(Gravity.CENTER, 0, 150);
                toast.show();
            }
        }


    }

}