using System.ComponentModel.DataAnnotations;

namespace backend.Models
{
    public class Product
    {
        [Key]
        public int productID { get; set; }
        public string name { get; set; }
        public string brand { get; set; }
        public string description { get; set; }
        public string imageURL { get; set; }

        public Product(int productID, string name, string brand, string description, string imageURL)
        {
            this.productID = productID;
            this.name = name;
            this.brand = brand;
            this.description = description;
            this.imageURL = imageURL;
        }
    }
}