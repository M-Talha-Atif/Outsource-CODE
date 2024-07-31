using backend.Data;
using backend.Models;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.IdentityModel.Tokens;
using System;
using System.Collections.Generic;
using System.IdentityModel.Tokens.Jwt;
using System.Linq;
using System.Security.Claims;
using System.Text;

namespace backend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    [EnableCors("_myAllowSpecificOrigins")]
    public class UserController : ControllerBase
    {
        private readonly IConfiguration _configuration;
        private readonly backendDbContext _dbContext;

        public UserController(IConfiguration configuration, backendDbContext dbContext)
        {
            _configuration = configuration;
            _dbContext = dbContext;
        }

        [HttpGet]
        public IActionResult Get()
        {
            IEnumerable<User> users = _dbContext.Users.ToList();
            return Ok(users);
        }

        [HttpGet("{userId}")]
        public IActionResult Get(int userId)
        {
            var user = _dbContext.Users.Find(userId);
            if (user == null)
            {
                return NotFound();
            }
            return Ok(user);
        }

        [HttpPost]
        public IActionResult Post(User newUser)
        {
            _dbContext.Users.Add(newUser);
            _dbContext.SaveChanges();
            return Ok();
        }

        [HttpPut("{userId}")]
        public IActionResult Put(int userId, User updatedUser)
        {
            if (userId != updatedUser.userID)
            {
                return BadRequest();
            }

            _dbContext.Entry(updatedUser).State = EntityState.Modified;

            try
            {
                _dbContext.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!_dbContext.Users.Any(u => u.userID == userId))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return Ok();
        }

        [HttpDelete("{userId}")]
        public IActionResult Delete(int userId)
        {
            var user = _dbContext.Users.Find(userId);
            if (user == null)
            {
                return NotFound();
            }

            _dbContext.Users.Remove(user);
            _dbContext.SaveChanges();

            return Ok();
        }

        [HttpPost("login")]
        public IActionResult Login(UserLoginRequest loginRequest)
        {
            var user = _dbContext.Users.FirstOrDefault(u => u.email == loginRequest.email);

            if (user == null || !user.CheckPassword(loginRequest.password))
            {
                return Unauthorized("Invalid username or password");
            }

            var jwtService = new JwtService(_configuration);
            var token = jwtService.GenerateJwtToken(user);

            return Ok(user.userID);
        }
    }
}
