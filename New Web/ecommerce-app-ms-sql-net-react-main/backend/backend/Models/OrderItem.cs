using System.ComponentModel.DataAnnotations;

namespace backend.Models
{
    public class OrderItem
    {
        [Key]
        public int orderItemID { get; set; }
        public int quantity { get; set; }
        public int orderID { get; set; }
        public int productSizeID { get; set; }

        public OrderItem(int orderItemID, int quantity, int orderID, int productSizeID)
        {
            this.orderItemID = orderItemID;
            this.quantity = quantity;
            this.orderID = orderID;
            this.productSizeID = productSizeID;
        }
    }
}
