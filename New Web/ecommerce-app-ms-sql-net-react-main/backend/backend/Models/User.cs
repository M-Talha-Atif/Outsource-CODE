using System.ComponentModel.DataAnnotations;
using System.Net;

namespace backend.Models
{
    public class User
    {
        [Key]
        public int userID { get; }
        public string firstName { get; set; }
        public string lastName { get; set; }
        public string email { get; set; }
        public string phone { get; set; }
        public string password { get; set; }

        public string address { get; set; }
        public string city { get; set; }
        public string postalCode { get; set; }
        public User()
        {

        }
        
        public User(int userId, string firstName, string lastName, string email, string phone, string password, string address = null, string city = null, string postalCode = null)
        {
            this.userID = userId;
            this.firstName = firstName;
            this.lastName = lastName;
            this.email = email;
            this.phone = phone;
            this.password = password;
            this.address = address;
            this.city = city;
            this.postalCode = postalCode;
        }
        public bool CheckPassword(string password)
        {
            return this.password == password; // temporary
        }
    }
}
