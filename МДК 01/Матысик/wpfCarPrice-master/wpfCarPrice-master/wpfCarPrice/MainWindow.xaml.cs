using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.AccessControl;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace wpfCarPrice
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        // Назначение глобальных переменных
        int finalCarPrice;
        int insurance;
        int carPrice;

        // Перемещение окна
        private void Window_MouseDown(object sender, MouseButtonEventArgs e)
        {
            
            if (e.ChangedButton == MouseButton.Left)
            {
                this.DragMove();
            }
        }

        public MainWindow()
        {
            InitializeComponent();

            // Назначение случайных значений
            Random random = new Random();

            carPrice = random.Next(1000000 , 5000000);
            insurance = random.Next(1000, 10000);

            // Вывод значенний
            finalCarPrice = carPrice;
            boxBasicPrice.Text = Convert.ToString(carPrice);
            boxFinalPrice.Text = Convert.ToString(carPrice);
            boxInsurance.Text = Convert.ToString(insurance);
        }

        // Обработчик на проверенные чекбоксы дополнительных опций
        private void cbAdditionals_Checked(object sender, RoutedEventArgs e)
        {
            CheckBox additons = e.OriginalSource as CheckBox;

            switch (additons.Name)
            {
                case "cbGPS":
                    finalCarPrice += 2500;
                    break;

                case "cbParking":
                    finalCarPrice += 2000;
                    break;

                case "cbLightDetector":
                    finalCarPrice += 3500;
                    break;

                case "cbBlueTooth":
                    finalCarPrice += 1000;
                    break;

                case "cbDVD":
                    finalCarPrice += 3000;
                    break;
            }
            
            boxFinalPrice.Text = Convert.ToString(finalCarPrice);
            boxOptionPrice.Text = Convert.ToString(finalCarPrice - carPrice);
        }

        // Обработчик на непроверенные чекбоксы дополнительных опций
        private void cbAdditionals_Unchecked(object sender, RoutedEventArgs e)
        {
            CheckBox additons = e.OriginalSource as CheckBox;

            switch (additons.Name)
            {
                case "cbGPS":
                    finalCarPrice -= 2500;
                    break;

                case "cbParking":
                    finalCarPrice -= 2000;
                    break;

                case "cbLightDetector":
                    finalCarPrice -= 3500;
                    break;

                case "cbBlueTooth":
                    finalCarPrice -= 1000;
                    break;

                case "cbDVD":
                    finalCarPrice -= 3000;
                    break;
            }
            
            boxFinalPrice.Text = Convert.ToString(finalCarPrice);
            boxOptionPrice.Text = Convert.ToString(finalCarPrice - carPrice);
        }

        // Обработчик на проверенный чекбоксы усилителя руля
        private void rbWheel_Checked(object sender, RoutedEventArgs e)
        {
            RadioButton wheel = e.OriginalSource as RadioButton;

            switch (wheel.Name)
            {
                case "rbNone":
                    
                    break;

                case "rbElectro":
                    finalCarPrice += 1000;
                    break;

                case "rbHydro":
                    finalCarPrice += 1500;
                    break;

                case "rbPneumatic":
                    finalCarPrice += 3000;
                    break;

                case "rbMech":
                    finalCarPrice += 500;
                    break;
            }

            boxFinalPrice.Text = Convert.ToString(finalCarPrice);
            boxOptionPrice.Text = Convert.ToString(finalCarPrice - carPrice);
        }

        // Обрабочик на непроверенные чекбоксы усилителя руля
        private void rbWheel_Unchecked(object sender, RoutedEventArgs e)
        {
            RadioButton wheel = e.OriginalSource as RadioButton;

            switch (wheel.Name)
            {
                case "rbElectro":
                    finalCarPrice -= 1000;
                    break;

                case "rbHydro":
                    finalCarPrice -= 1500;
                    break;

                case "rbPneumatic":
                    finalCarPrice -= 3000;
                    break;

                case "rbMech":
                    finalCarPrice -= 500;
                    break;
            }

            boxFinalPrice.Text = Convert.ToString(finalCarPrice);
            boxOptionPrice.Text = Convert.ToString(finalCarPrice - carPrice);
        }

        // Обработчик на страховку
        bool error = false;
        private void cb3Insurance_Checked(object sender, RoutedEventArgs e)
        {

            try
            {
                insurance = Convert.ToInt32(boxInsurance.Text);
            }
            catch (FormatException)
            {
                MessageBox.Show("Введите корректное значение в виде цифр", "Ошибка!");
                error = true;
                return;
            }

            error = false;

            if (insurance < 0)
            {
                cb3Insurance.IsChecked = false;
                MessageBox.Show("Страховка не может быть меньше нуля");

            }
            else if (insurance > 10000)
            {
                cb3Insurance.IsChecked = false;
                MessageBox.Show("Страховка не может быть такой большой");
            }
            else
            {
                finalCarPrice += insurance;
                boxFinalPrice.Text = Convert.ToString(finalCarPrice);
                boxOptionPrice.Text = Convert.ToString(finalCarPrice - carPrice);
            }
            
        }

        // Обработчик на снятие страховки
        private void cb3Insurance_Unchecked(object sender, RoutedEventArgs e)
        {
            if (error == true)
            {

            }
            else
            {
                if (insurance <= 0 || insurance > 10000)
                {

                }
                else
                {
                    finalCarPrice -= insurance;
                    boxFinalPrice.Text = Convert.ToString(finalCarPrice);
                    boxOptionPrice.Text = Convert.ToString(finalCarPrice - carPrice);
                }
            }

            
        }

        // Назначение переменных количества  для опций с количеством
        int count1 = 0;
        int count2 = 0;
        int count3 = 0;
        int count4 = 0;
        int count5 = 0;

        // Увеличение или уменьшение количества
        private void btCount_Click(object sender, RoutedEventArgs e)
        {
            Button btcount = e.OriginalSource as Button;

            switch (btcount.Name)
            {
                case "btCountPlus1":
                    if (count1 < 4)
                    {
                        count1++;
                    }
                    break;

                case "btCountPlus2":
                    if (count2 < 4)
                    {
                        count2++;
                    }
                    break;

                case "btCountPlus3":
                    if (count3 < 2)
                    {
                        count3++;
                    }
                    break;

                case "btCountPlus4":
                    if (count4 < 2)
                    {
                        count4++;
                    }
                    break;

                case "btCountPlus5":
                    if (count5 < 4)
                    {
                        count5++;
                    }
                    break;
            }

            switch (btcount.Name)
            {
                case "btCountMinus1":
                    count1 = minusCount(count1);
                    break;

                case "btCountMinus2":
                    count2 = minusCount(count2);
                    break;

                case "btCountMinus3":
                    count3 = minusCount(count3);
                    break;

                case "btCountMinus4":
                    count4 = minusCount(count4);
                    break;

                case "btCountMinus5":
                    count5 = minusCount(count5);
                    break;
            }


            boxCountOptions1.Text = Convert.ToString(count1);
            boxCountOptions2.Text = Convert.ToString(count2);
            boxCountOptions3.Text = Convert.ToString(count3);
            boxCountOptions4.Text = Convert.ToString(count4);
            boxCountOptions5.Text = Convert.ToString(count5);
        }

        // Функция проверки вычитания чтобы не уйти в минус
        private int minusCount(int value)
        {
            if (value > 0)
            {
                return value - 1;
            }
            else
            {
                return value;
            }
        }

        // Обработчик для чекбокосов опций с количествос
        private void cb2_Checked(object sender, RoutedEventArgs e)
        {
            CheckBox countOptions = e.OriginalSource as CheckBox;

            switch (countOptions.Name)
            {
                case "cb2AntiFog":
                    finalCarPrice += count1 * 1000;
                    boxCountOptions1.IsEnabled = false;
                    btCount1.IsEnabled = false;
                    break;

                case "cb2ChairHeat":
                    finalCarPrice += count2 * 500;
                    boxCountOptions2.IsEnabled = false;
                    btCount2.IsEnabled = false;
                    break;

                case "cb2Camera":
                    finalCarPrice += count3 * 10000;
                    boxCountOptions3.IsEnabled = false;
                    btCount3.IsEnabled = false;
                    break;

                case "cb2MirrorsHear":
                    finalCarPrice += count4 * 5000;
                    boxCountOptions4.IsEnabled = false;
                    btCount4.IsEnabled = false;
                    break;

                case "cb2HeadlightClean":
                    finalCarPrice += count5 * 1000;
                    boxCountOptions5.IsEnabled = false;
                    btCount5.IsEnabled = false;
                    break;
            }

            boxFinalPrice.Text = Convert.ToString(finalCarPrice);
            boxOptionPrice.Text = Convert.ToString(finalCarPrice - carPrice);
        }

        // Обработчик для чекбокосов опций с количеством
        private void cb2_Unchecked(object sender, RoutedEventArgs e)
        {
            CheckBox countOptions = e.OriginalSource as CheckBox;

            switch (countOptions.Name)
            {
                case "cb2AntiFog":
                    finalCarPrice -= count1 * 1000;
                    boxCountOptions1.IsEnabled = true;
                    btCount1.IsEnabled = true;
                    break;

                case "cb2ChairHeat":
                    finalCarPrice -= count2 * 500;
                    boxCountOptions2.IsEnabled = true;
                    btCount2.IsEnabled = true;
                    break;

                case "cb2Camera":
                    finalCarPrice -= count3 * 10000;
                    boxCountOptions3.IsEnabled = true;
                    btCount3.IsEnabled = true;
                    break;

                case "cb2MirrorsHear":
                    finalCarPrice -= count4 * 5000;
                    boxCountOptions4.IsEnabled = true;
                    btCount4.IsEnabled = true;
                    break;

                case "cb2HeadlightClean":
                    finalCarPrice -= count5 * 1000;
                    boxCountOptions5.IsEnabled = true;
                    btCount5.IsEnabled = true;
                    break;
            }

            boxFinalPrice.Text = Convert.ToString(finalCarPrice);
            boxOptionPrice.Text = Convert.ToString(finalCarPrice - carPrice);
        }
    }
}
