using Npgsql;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Xml.Linq;

namespace ComputerShop
{
    internal class Database
    {
        private static string constring = "Host=localhost;Username=postgres;Password=VEST777berto;Database=postgres";


        public static async Task<List<item>> getItems(item item)
        {
            var data = new List<item>();

            string query = "SELECT * FROM computer_shop.item WHERE 1=1";

            if (item != null)
            {
                if (item.id.HasValue)
                {
                    query += $" AND id = {item.id}";
                }

                if (item.cost.HasValue)
                {
                    query += $" AND cost >= {item.cost}";
                }

                if (item.maxCost.HasValue)
                {
                    query += $" AND cost <= {item.maxCost}";
                }

                if (!string.IsNullOrEmpty(item.name))
                {
                    query += $" AND name = @name";
                }
            }


            using (var conn = new NpgsqlConnection(constring))
            {
                await conn.OpenAsync();
                
                using (var cmd = new NpgsqlCommand(query, conn))
                {
                    if (item != null)
                    {
                        cmd.Parameters.AddWithValue("@name", item.name);
                    }

                    var reader = await cmd.ExecuteReaderAsync();

                    while (await reader.ReadAsync())
                    {
                        data.Add(new item
                        {
                            id = reader.GetInt32(0),
                            description = reader.GetString(1),
                            cost = reader.GetInt32(2),
                            name = reader.GetString(3)
                        });
                    }
                    return data;
                }
            }
        }
        public static async Task<bool> login(string username, string password)
        {
            using (var conn = new NpgsqlConnection(constring))
            {
                await conn.OpenAsync();
                string query = "SELECT COUNT(login) FROM computer_shop.admin WHERE login = @username AND password = @password;";

                using (var cmd = new NpgsqlCommand(query, conn))
                {
                    cmd.Parameters.AddWithValue("@username", username);
                    cmd.Parameters.AddWithValue("@password", password);

                    

                    if (Convert.ToInt64(await cmd.ExecuteScalarAsync()) == 1)
                    {
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                    
                }
            }
        }

        public static async Task<bool> deleteItem(item item)
        {
            using (var conn = new NpgsqlConnection(constring))
            {
                await conn.OpenAsync();
                string query = "DELETE FROM computer_shop.item WHERE id = @id OR name = @name;";

                using (var cmd = new NpgsqlCommand(query, conn))
                {
                    cmd.Parameters.AddWithValue("@id", item.id);
                    cmd.Parameters.AddWithValue("@name", item.name);

                    var test = Convert.ToInt64(await cmd.ExecuteNonQueryAsync());

                    if (test == 1)
                    {
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }


        public static async Task<bool> addItem(item item)
        {
            using (var conn = new NpgsqlConnection(constring))
            {
                await conn.OpenAsync();
                string query = "INSERT INTO computer_shop.item  (description, cost, name) VALUES (@description, @cost, @name);";

                using (var cmd = new NpgsqlCommand(query, conn))
                {
                    cmd.Parameters.AddWithValue("@description", item.description);
                    cmd.Parameters.AddWithValue("@name", item.name);
                    cmd.Parameters.AddWithValue("@cost", item.cost);

                    var test = Convert.ToInt64(await cmd.ExecuteNonQueryAsync());

                    if (test == 1)
                    {
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
    }
}
