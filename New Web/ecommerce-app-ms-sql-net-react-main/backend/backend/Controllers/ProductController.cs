using backend.Data;
using backend.Models;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using Microsoft.CodeAnalysis;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Newtonsoft.Json;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;


namespace backend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    [EnableCors("_myAllowSpecificOrigins")]

    public class ProductController : ControllerBase
    {
        private readonly backendDbContext _dbContext;

        public ProductController(backendDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        [HttpGet]
        public IActionResult Get()
        {
            IEnumerable<Product> products = _dbContext.Products.ToList();
            return Ok(products);
        }

        [HttpGet("{productId}")]
        public IActionResult Get(int productId)
        {
            var product = _dbContext.Products.FirstOrDefault(x => x.productID == productId);
            if (product == null)
            {
                return NotFound();
            }
            return Ok(product);
        }

        [HttpPost]
        public IActionResult Post(Product product)
        {
            _dbContext.Products.Add(product);
            _dbContext.SaveChanges();
            return Ok();
        }

         [HttpPut("{productId}")]
        public IActionResult Put(int productId, [FromBody] Product updatedProduct)
        {
            if (productId != updatedProduct.productID)
            {
                return BadRequest();
            }

            _dbContext.Entry(updatedProduct).State = EntityState.Modified;

            try
            {
                _dbContext.SaveChanges();
                return Ok();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!_dbContext.Products.Any(p => p.productID == productId))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }


        [HttpDelete("{productId}")]
        public IActionResult Delete(int productId)
        {
            var product = _dbContext.Products.Find(productId);
            if (product == null)
            {
                return NotFound();
            }

            _dbContext.Products.Remove(product);
            _dbContext.SaveChanges();

            return Ok();
        }
    }
}
