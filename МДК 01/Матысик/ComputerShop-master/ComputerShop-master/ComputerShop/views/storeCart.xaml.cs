using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace ComputerShop.views
{
    /// <summary>
    /// Логика взаимодействия для storeCart.xaml
    /// </summary>
    public partial class storeCart : Window
    {
        public int cash {  get; set; }
        public storeCart(int cash)
        {
            InitializeComponent();
            tbBalance.Text = $"Баланс на карте: {cash}";
        }

        private void btReturn_Click(object sender, RoutedEventArgs e)
        {
            Window window = new MainWindow();
            window.Show();
            this.Hide();
        }

        private void btForm_Click(object sender, RoutedEventArgs e)
        {
            Window window = new formOrder();
            window.Show();
            this.Hide();
        }
    }
}
