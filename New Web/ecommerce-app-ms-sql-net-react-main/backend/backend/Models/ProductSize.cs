using System.ComponentModel.DataAnnotations;

namespace backend.Models
{
    public class ProductSize
    {
        [Key]
        public int productSizeID { get; set; }
        public int size { get; set; }
        public decimal price { get; set; }
        public int quantity { get; set; }
        public int productID { get; set; }

        public ProductSize(int productSizeID, int size, decimal price, int quantity, int productID )
        {
            this.productSizeID = productSizeID;
            this.size = size;
            this.price = price;
            this.quantity = quantity;
            this.productID = productID;
        }
    }
}
