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
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Drawing;
using System.Windows.Forms.DataVisualization.Charting;
using System.Text.RegularExpressions;
using System.Runtime.Serialization;

namespace graph_wps
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

        private Series series;
        private Series seriessin;
        private Series seriescos;

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            chart.ChartAreas.Add(new ChartArea("SeriaArena"));

            series = new Series("Seria");
            series.ChartType = SeriesChartType.Line;
            series.LegendText = "y=k1*sin(k2*x+k3)+k4";
            chart.Series.Add(series);
            chart.Series["Seria"].ChartArea = "SeriaArena";

            seriessin = new Series("Sin");
            seriessin.ChartType = SeriesChartType.Line;
            series.LegendText = "y=sin(x)";
            chart.Series.Add(seriessin);
            chart.Series["Sin"].ChartArea = "SeriaArena";

            seriescos = new Series("Cos");
            seriescos.ChartType = SeriesChartType.Line;
            seriescos.LegendText = "y=cos(x)";
            chart.Series.Add(seriescos);
            chart.Series["Cos"].ChartArea = "SeriaArena";

            Legend legend = new Legend();
            legend.Name = "legend";
            legend.Font = new Font("Arial", 13);
            chart.Legends.Add(legend);
            chart.Legends["legend"].Docking = Docking.Top;

        }



        private void Button_Click(object sender, RoutedEventArgs e)
        {
            series.IsVisibleInLegend = false;
            seriessin.IsVisibleInLegend = false;
            seriescos.IsVisibleInLegend = false;

            chart.Series["Seria"].Points.Clear();
            chart.Series["Sin"].Points.Clear();
            chart.Series["Cos"].Points.Clear();

            tbForText.Clear();

            if (cbY1.IsChecked == true)
            {
                double x, y, a, b, h, k1, k2, k3, k4;

                try
                {
                    a = Convert.ToDouble(tbA.Text);
                    b = Convert.ToDouble(tbB.Text);
                    h = Convert.ToDouble(tbH.Text);
                    k1 = Convert.ToDouble(tbK1.Text);
                    k2 = Convert.ToDouble(tbK2.Text);
                    k3 = Convert.ToDouble(tbK3.Text);
                    k4 = Convert.ToDouble(tbK4.Text);
                }
                catch (FormatException)
                {
                    MessageBox.Show("Введите корректное значение", "Неправильный формат данные");
                    return;
                }

                x = a;

                string text = "";

                while (x <= b)
                {
                    y = k1 * Math.Sin(k2 * x + k3) + k4;
                    series.Points.AddXY(x, y);
                    text += $"X:{Math.Round(x, 2)} Y:{Math.Round(y, 2)}" + Environment.NewLine; 
                    x += h;
                }
                tbForText.Text = Environment.NewLine + "График y=k*sin(k2*x+k3)+k4" + Environment.NewLine + text;

                series.IsVisibleInLegend = true;
            }

            if (cbY2.IsChecked == true)
            {
                double x, y, a, b, h;

                try 
                {
                    a = Convert.ToDouble(tbA.Text);
                    b = Convert.ToDouble(tbB.Text);
                    h = Convert.ToDouble(tbH.Text);
                }
                catch (FormatException)
                {
                    MessageBox.Show("Введите корректное значение", "Неправильный формат данные");
                    return;
                }

                x = a;
                string text = "";

                while (x <= b)
                {
                    y = Math.Sin(x);
                    seriessin.Points.AddXY(x, y);
                    text += $"X:{Math.Round(x, 2)} Y:{Math.Round(y, 2)}" + Environment.NewLine;
                    x += h;
                }

                tbForText.Text += Environment.NewLine + "График y=sin(x)" + Environment.NewLine + text;

                seriessin.IsVisibleInLegend = true;
            }

            if (cbY3.IsChecked == true)
            {
                double x, y, a, b, h;

                try
                {
                    a = Convert.ToDouble(tbA.Text);
                    b = Convert.ToDouble(tbB.Text);
                    h = Convert.ToDouble(tbH.Text);

                }
                catch (FormatException)
                {
                    MessageBox.Show("Введите корректное значение", "Неправильный формат данные");
                    return;
                }

                x = a;
                string text = "";

                while (x <= b)
                {
                    y = Math.Cos(x);
                    seriescos.Points.AddXY(x, y);
                    text += $"X:{Math.Round(x, 2)} Y:{Math.Round(y, 2)}" + Environment.NewLine;
                    x += h;
                }

                tbForText.Text += Environment.NewLine + "График y=cos(x)" + Environment.NewLine + text;

                seriescos.IsVisibleInLegend = true;
            }

            
        }

        private void btClear_Click(object sender, RoutedEventArgs e)
        {
            chart.Series["Seria"].Points.Clear();
            chart.Series["Sin"].Points.Clear();
            chart.Series["Cos"].Points.Clear();
            tbK1.Clear();
            tbK2.Clear();
            tbK3.Clear();
            tbK4.Clear();
            tbA.Clear();
            tbB.Clear();
            tbH.Clear();
            tbForText.Clear();
        }

        private void tbK1_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = !Regex.IsMatch(e.Text, @"[\d\+\-\,]");
        }

        private void tbK2_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = !Regex.IsMatch(e.Text, @"[\d\+\-\,]");
        }

        private void tbK3_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = !Regex.IsMatch(e.Text, @"[\d\+\-\,]");
        }

        private void tbK4_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = !Regex.IsMatch(e.Text, @"[\d\+\-\,]");
        }

        private void tbA_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = !Regex.IsMatch(e.Text, @"[\d\+\-\,]");
        }

        private void tbB_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = !Regex.IsMatch(e.Text, @"[\d\+\-\,]");
        }

        private void tbH_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = !Regex.IsMatch(e.Text, @"[\d\+\-\,]");
        }
    }
}

