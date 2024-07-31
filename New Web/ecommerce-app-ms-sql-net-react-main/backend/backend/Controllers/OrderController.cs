using backend.Data;
using backend.Models;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;

namespace backend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    [EnableCors("_myAllowSpecificOrigins")]
    public class OrderController : ControllerBase
    {
        private readonly backendDbContext _dbContext;

        public OrderController(backendDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        [HttpGet]
        public IActionResult Get()
        {
            IEnumerable<Order> orders = _dbContext.Orders.ToList();
            return Ok(orders);
        }

        [HttpGet("{userId}")]
        public IActionResult Get(int userId)
        {
            var orders = _dbContext.Orders.Where(o => o.userID == userId).ToList();
            if (orders == null || orders.Count == 0)
            {
                return NotFound();
            }
            return Ok(orders);
        }

        [HttpPost]
        public IActionResult Post(Order newOrder)
        {
            newOrder.dateTime = DateTime.Now;
            _dbContext.Orders.Add(newOrder);
            _dbContext.SaveChanges();
            return Ok();
        }

        [HttpPut("{orderId}")]
        public IActionResult Put(int orderId, Order updatedOrder)
        {
            if (orderId != updatedOrder.orderID)
            {
                return BadRequest();
            }

            _dbContext.Entry(updatedOrder).State = EntityState.Modified;

            try
            {
                _dbContext.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!_dbContext.Orders.Any(o => o.orderID == orderId))
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

        [HttpDelete("{orderId}")]
        public IActionResult Delete(int orderId)
        {
            var order = _dbContext.Orders.Find(orderId);
            if (order == null)
            {
                return NotFound();
            }

            _dbContext.Orders.Remove(order);
            _dbContext.SaveChanges();

            return Ok();
        }
    }
}
