using ComputerShop.views;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Automation.Peers;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ComputerShop
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

        private void btAdmin_Click(object sender, RoutedEventArgs e)
        {
            Window login = new login();
            login.Show();
            this.Hide();
        }

        private void btOrder_Click(object sender, RoutedEventArgs e)
        {
            Random random = new Random();
            int cash = random.Next(5000, 140000);

            storeCart storeCart = new storeCart(cash);
            storeCart.Show();

            this.Hide();            
        }

        private void btPrice_Click(object sender, RoutedEventArgs e)
        {
            Window catalog = new catalog();
            catalog.Show();
            this.Hide();
        }
    }
}
