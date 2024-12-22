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
    /// Логика взаимодействия для catalog.xaml
    /// </summary>
    public partial class catalog : Window
    {

        public async Task loadItems()
        {
            item item = null;
            var data = await Database.getItems(item);
            itemGrid.ItemsSource = data;
        }
        public catalog()
        {
            InitializeComponent();
            loadItems();
        }

        private void btReturnCatalog_Click(object sender, RoutedEventArgs e)
        {
            Window window = new MainWindow();
            window.Show();
            this.Hide();
        }

        private async void btSearch_Click(object sender, RoutedEventArgs e)
        {
            string name;

            int? id = string.IsNullOrWhiteSpace(tbId.Text) ? (int?)null : Convert.ToInt32(tbId.Text);
            int? minPrice = string.IsNullOrWhiteSpace(tbPriceMin.Text) ? (int?)null : Convert.ToInt32(tbPriceMin.Text);
            int? maxPrice = string.IsNullOrWhiteSpace(tbPriceMax.Text) ? (int?)null : Convert.ToInt32(tbPriceMax.Text);

            name = tbName.Text;

            item item = new item
            {
                id = id,
                cost = minPrice,
                maxCost = maxPrice,
                name = name
            };

            var data = await Database.getItems(item);
            itemGrid.ItemsSource = data;






        }

        private void tbreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = new Regex("[^0-9]+").IsMatch(e.Text);
        }

    }
}
