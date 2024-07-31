using backend.Data;
using backend.Models;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.Linq;

namespace backend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    [EnableCors("_myAllowSpecificOrigins")]
    public class OrderItemController : ControllerBase
    {
        private readonly backendDbContext _dbContext;

        public OrderItemController(backendDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        [HttpGet]
        public IActionResult Get()
        {
            IEnumerable<OrderItem> orderItems = _dbContext.OrderItems.ToList();
            return Ok(orderItems);
        }

        [HttpGet("{orderId}")]
        public IActionResult Get(int orderId)
        {
            var orderItems = _dbContext.OrderItems.Where(oi => oi.orderID == orderId).ToList();
            if (orderItems == null || orderItems.Count == 0)
            {
                return NotFound();
            }
            return Ok(orderItems);
        }

        [HttpPost]
        public IActionResult Post(OrderItem orderItem)
        {
            _dbContext.OrderItems.Add(orderItem);
            _dbContext.SaveChanges();
            return Ok();
        }

        [HttpPut("{orderItemId}")]
        public IActionResult Put(int orderItemId, OrderItem updatedOrderItem)
        {
            if (orderItemId != updatedOrderItem.orderItemID)
            {
                return BadRequest();
            }

            _dbContext.Entry(updatedOrderItem).State = EntityState.Modified;

            try
            {
                _dbContext.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!_dbContext.OrderItems.Any(oi => oi.orderItemID == orderItemId))
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

        [HttpDelete("{orderItemId}")]
        public IActionResult Delete(int orderItemId)
        {
            var orderItem = _dbContext.OrderItems.Find(orderItemId);
            if (orderItem == null)
            {
                return NotFound();
            }

            _dbContext.OrderItems.Remove(orderItem);
            _dbContext.SaveChanges();

            return Ok();
        }
    }
}
