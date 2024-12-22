using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            var currentButton = sender as Button;
            text.Text += currentButton.Text;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            var res = new DataTable();
            text.Text = res.Compute(text.Text, "").ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            text.Clear();
        }

        private void button19_Click(object sender, EventArgs e)
        {
            var str = "";
            for (int i = 0; i < text.Text.Length - 1; i++)
            {
                str += text.Text[i];
            }
            text.Text = str;
        }
        public bool znak = true;
        private void button5_Click(object sender, EventArgs e)
        {
            if (znak == true)
            {
                znak = false;
                text.Text = "-" + text.Text;
            }
            else 
            {
                var del = text.Text;
                text.Text = del.Replace("-", string.Empty);
                znak = true;
            }

        }
    }
}
