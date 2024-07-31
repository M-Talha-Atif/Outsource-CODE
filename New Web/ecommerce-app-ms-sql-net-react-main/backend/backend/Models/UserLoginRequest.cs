using System.ComponentModel.DataAnnotations;

namespace backend.Models
{
    public class UserLoginRequest
    {
        [Key]
        public int Id { get; set; }
        public string email { get; set; }
        public string password { get; set; }
    }
}
