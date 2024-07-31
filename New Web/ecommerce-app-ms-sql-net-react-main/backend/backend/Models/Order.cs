using System.ComponentModel.DataAnnotations;

namespace backend.Models
{
    public enum OrderStatus
    {
        Pending,
        Processing,
        Shipped,
        Delivered,
        Cancelled,
    }

    public class Order
    {
        [Key]
        public int orderID { get; set; }
        public DateTime dateTime { get; set; }
        public decimal totalPrice { get; set; }
        public OrderStatus status { get; set; }
        public int userID { get; set; }

        public Order(int orderID, DateTime dateTime, decimal totalPrice, OrderStatus status, int userID)
        {
            this.orderID = orderID;
            this.dateTime = dateTime;
            this.totalPrice = totalPrice;
            this.status = status;
            this.userID = userID;
        }
    }
}
