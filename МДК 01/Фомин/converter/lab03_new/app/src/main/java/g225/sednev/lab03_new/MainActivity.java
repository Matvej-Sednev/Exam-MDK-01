package g225.sednev.lab03_new;
import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Spinner;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;



public class MainActivity extends AppCompatActivity {

    EditText number;
    TextView vivod;
    Spinner spin1, spin2;



    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        spin1 = findViewById(R.id.spin1);
        spin2 = findViewById(R.id.spin2);
        ArrayAdapter<Unit> adp = new ArrayAdapter<Unit>(this, android.R.layout.simple_list_item_1);



        RadioGroup radioGroup = findViewById(R.id.radiobutton);
        RadioButton mass = findViewById(R.id.mass);
        RadioButton distance = findViewById(R.id.distance);
        RadioButton volume = findViewById(R.id.volume);
        radioGroup.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId){
                adp.clear();
                if (checkedId == R.id.mass)
                {
                    adp.add(new Unit("g", 1000.0));
                    adp.add(new Unit("kg", 1));
                    adp.add(new Unit("cwt", 0.01));
                    adp.add(new Unit("t", 0.001));

                }
                else if (checkedId==R.id.distance)
                {


                    adp.add(new Unit("mm", 1000.0));
                    adp.add(new Unit("cm", 100));
                    adp.add(new Unit("m", 1));
                    adp.add(new Unit("km", 0.001));
                }
                else if (checkedId==R.id.volume)
                {

                    adp.add(new Unit("ml", 1000.0));
                    adp.add(new Unit("l", 1));
                    adp.add(new Unit("m^3", 0.001));

                }
            }
        });



        number = findViewById(R.id.number);
        vivod = findViewById(R.id.vivod);
        spin1.setAdapter(adp);
        spin2.setAdapter(adp);

    }
    public void convert_click(View view)
    {
        Unit sfrom = (Unit) spin1.getSelectedItem();
        Unit sto = (Unit) spin2.getSelectedItem();

        try {
            if (Float.parseFloat(number.getText().toString()) < 0){
                vivod.setText("Ошибка ввода числа");
                return;
            }
            float from = Float.parseFloat(number.getText().toString());
            double to = from / sfrom.coeff * sto.coeff;

            vivod.setText(String.valueOf(to));
        } catch (NumberFormatException e) {
            vivod.setText("Ошибка ввода числа");
        }








    }
}