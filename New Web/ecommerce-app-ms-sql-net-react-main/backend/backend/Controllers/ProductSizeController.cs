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
    public class ProductSizeController : ControllerBase
    {
        private readonly backendDbContext _dbContext;

        public ProductSizeController(backendDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        [HttpGet]
        public IActionResult Get()
        {
            IEnumerable<ProductSize> productSizes = _dbContext.ProductSizes.ToList();
            return Ok(productSizes);
        }

        [HttpGet("{productId}")]
        public IActionResult Get(int productId)
        {
            var productSizes = _dbContext.ProductSizes.Where(ps => ps.productID == productId).ToList();
            if (productSizes == null || !productSizes.Any())
            {
                return NotFound();
            }
            return Ok(productSizes);
        }

        [HttpGet("{productSizeId}/size")]
        public IActionResult GetProductSizeById(int productSizeId)
        {
            var productSize = _dbContext.ProductSizes.FirstOrDefault(ps => ps.productSizeID == productSizeId);
            if (productSize == null)
            {
                return NotFound();
            }
            return Ok(productSize);
        }

        [HttpPost]
        public IActionResult Post(ProductSize newProductSize)
        {
            _dbContext.ProductSizes.Add(newProductSize);
            _dbContext.SaveChanges();
            return Ok();
        }

        [HttpPut("{productSizeId}")]
        public IActionResult Put(int productSizeId, ProductSize updatedProductSize)
        {
            if (productSizeId != updatedProductSize.productSizeID)
            {
                return BadRequest();
            }

            _dbContext.Entry(updatedProductSize).State = EntityState.Modified;

            try
            {
                _dbContext.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!_dbContext.ProductSizes.Any(ps => ps.productSizeID == productSizeId))
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

        [HttpDelete("{productSizeId}")]
        public IActionResult Delete(int productSizeId)
        {
            var productSize = _dbContext.ProductSizes.Find(productSizeId);
            if (productSize == null)
            {
                return NotFound();
            }

            _dbContext.ProductSizes.Remove(productSize);
            _dbContext.SaveChanges();

            return Ok();
        }
    }
}
