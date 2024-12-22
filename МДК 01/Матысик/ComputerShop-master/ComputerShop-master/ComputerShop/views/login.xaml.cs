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
    /// Логика взаимодействия для login.xaml
    /// </summary>
    public partial class login : Window
    {
        public login()
        {
            InitializeComponent();
        }

        private void btReturnAdmin_Click(object sender, RoutedEventArgs e)
        {
            Window window = new MainWindow();
            window.Show();
            this.Close();
        }

        private async void btLogin_Click(object sender, RoutedEventArgs e)
        {
            if (await Database.login(tbLogin.Text, tbPassword.Password) == true)
            {
                Window admin = new admin();
                admin.Show();
                this.Close();
            }
            else
            {
                MessageBox.Show("Неверный логин или пароль");
            }


            
        }
    }
}
