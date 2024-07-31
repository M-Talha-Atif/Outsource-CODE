using backend.Models;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

namespace backend
{
    public interface IJwtService
    {
        string GenerateJwtToken(User user);
    }

    public class JwtService : IJwtService
    {
        private readonly IConfiguration _configuration;

        public JwtService(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        public string GenerateJwtToken(User user)
        {
            var tokenHandler = new JwtSecurityTokenHandler();
            var key = Encoding.ASCII.GetBytes(_configuration["Jwt:Secret"]); 
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new ClaimsIdentity(new Claim[]
                {
                    new Claim(ClaimTypes.NameIdentifier, user.userID.ToString()),
                    new Claim(ClaimTypes.Name, user.firstName),
                    new Claim(ClaimTypes.Surname, user.lastName),
                    new Claim(ClaimTypes.Email, user.email),
                    new Claim(ClaimTypes.MobilePhone, user.phone),
                    new Claim(ClaimTypes.StreetAddress, user.address ?? ""),    
                    new Claim(ClaimTypes.Locality, user.city ?? ""),
                    new Claim(ClaimTypes.PostalCode, user.postalCode ?? "")
                }),
                Expires = DateTime.UtcNow.AddHours(1),
                NotBefore = DateTime.UtcNow,
                SigningCredentials = new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256Signature)
            };
            var token = tokenHandler.CreateToken(tokenDescriptor);
            return tokenHandler.WriteToken(token);
        }
    }
}