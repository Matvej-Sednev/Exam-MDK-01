using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
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
    /// Логика взаимодействия для admin.xaml
    /// </summary>
    public partial class admin : Window
    {
        public admin()
        {
            InitializeComponent();
        }

        private void btReturn_Click(object sender, RoutedEventArgs e)
        {
            
        }

        private async void btAddPos_Click(object sender, RoutedEventArgs e)
        {

            if (string.IsNullOrEmpty(tbAddName.Text) || string.IsNullOrEmpty(tbAddDesc.Text) || Convert.ToInt32(tbAddCost.Text) == null)
            {
                MessageBox.Show("Введите корректные данные");
                
            }
            else
            {
                var item = new item
                {
                    id = Convert.ToInt32(tbAddCost.Text),
                    description = tbAddDesc.Text,
                    name = tbAddName.Text
                };

                if (await Database.addItem(item) != true)
                {
                    MessageBox.Show("Что-то пошло не так...");
                }
                else
                {

                }
            }
        }

        private void btEditPos_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrEmpty(tbEditDesc.Text) || string.IsNullOrEmpty(tbEditName.Text) || Convert.ToInt32(tbEditCost.Text) == null)
            {
                MessageBox.Show("Введите корректные данные");
            }
            else
            {

            }
        }

        private async void btDelPos_Click(object sender, RoutedEventArgs e)
        {
            var item = new item
            {
                id = string.IsNullOrWhiteSpace(tbDelId.Text) ? 0 : Convert.ToInt32(tbDelId.Text),
                name = tbDelName.Text
            };

            
            if (await Database.deleteItem(item) != true)
            {
                MessageBox.Show("Введите существующую позицию");
            }
            else
            {
                MessageBox.Show("Позиция удалена");
            }

        }

        private void btExport_Click(object sender, RoutedEventArgs e)
        {

        }

        

        private void tbAddCost_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = new Regex("[^0-9]+").IsMatch(e.Text);
        }

        private void tbDelId_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = new Regex("[^0-9]+").IsMatch(e.Text);
        }
    }
}
