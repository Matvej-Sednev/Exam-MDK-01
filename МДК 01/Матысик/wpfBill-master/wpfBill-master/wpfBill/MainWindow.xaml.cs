using QRCoder;
using QRCoder.Xaml;
using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media;

namespace wpfBill
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        // Назначение переменных
        double price, discountP, discount, priceResult;
        int count;
        string finalResult, pred, file, product;
        string time = DateTime.Now.ToString("yyyy-MM-dd_HH-mm");
        

        // Кнопка "распечатать" текст
        private void btRaspBill_Click(object sender, RoutedEventArgs e)
        {
            
            string name = $"bill_{time}.txt";
            string filePath = System.IO.Path.Combine("C:\\Users\\zadro\\source\\repos\\wpfBill\\wpfBill\\", name);
            file = boxBill.Text;
            File.WriteAllText(filePath, file);
        }

        // Кнопка очистить
        private void boxClear_Click(object sender, RoutedEventArgs e)
        {
            boxBill.Clear();
            pred = null;
            finalResult = null;
            priceResult = 0;
            finalPriceResult = 0;
            imageQRCode.Source = null;
        }

        // Ограничение на ввод только цифр
        private void boxDiscount_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = new Regex("[^0-9]+").IsMatch(e.Text);
        }

        private void boxCount_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = new Regex("[^0-9]+").IsMatch(e.Text);
        }

        private void boxPrice_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = new Regex("[^0-9]+").IsMatch(e.Text);
        }

        double finalPriceResult = 0;
        // Основная кнопка "добавить в корзину
        private void boxAddBill_Click(object sender, RoutedEventArgs e)
        {
            // Ввод данных продукта
            product = boxProduct.Text;
            price = Convert.ToDouble(boxPrice.Text);
            count = Convert.ToInt32(boxCount.Text);

            // Контроль ввода скидки
            if (!string.IsNullOrEmpty(boxDiscount.Text))
            {
                discount = Convert.ToInt32(boxDiscount.Text);
            }
            
            // Расчёт скидки
            discountP = discount / 100;

            // Добавление прошлых товаров если они есть
            boxBill.Text = pred;

            // Рассчёт скидки
            if (!string.IsNullOrEmpty(boxDiscount.Text))
            {
                priceResult = ((price - (price * discountP)) * count);
            }
            else
            {
                priceResult = price * count;
            }
            
            //  Итоговый вывод
            boxBill.Text += $"Товар: {product}" + Environment.NewLine + $"Цена: {price}" + Environment.NewLine + $"Количество: {count}" + Environment.NewLine;
            if (!string.IsNullOrEmpty(boxDiscount.Text))
            {
                boxBill.Text += $"Скидка: {discount}%" + Environment.NewLine;
            }
            boxBill.Text += $"Итого: {priceResult}" + Environment.NewLine;
            boxBill.Text += "--------------------------------------------" + Environment.NewLine;
            finalPriceResult += priceResult;
            finalResult = $"Конечная сумма: {finalPriceResult}" + Environment.NewLine + "--------------------------------------------" + Environment.NewLine; ;

            // Запись для последующих товаров
            pred = boxBill.Text;

            // Увеличение финальной суммы
            boxBill.Text += finalResult;

            // Сброс значений скидки
            discount = 100 ; discountP = 1;

            // Генерация и вывод qrcode 
            QRCodeGenerator QRgenerator = new QRCodeGenerator();
            QRCodeData qrCodeData = QRgenerator.CreateQrCode("--------------------------------------------" + Environment.NewLine + $"Чек на:{time}" + Environment.NewLine + finalResult, QRCodeGenerator.ECCLevel.M);
            XamlQRCode qrCode = new XamlQRCode(qrCodeData);
            DrawingImage qrcodexaml = qrCode.GetGraphic(20);

            imageQRCode.Source = qrcodexaml;
        }
    }
}
