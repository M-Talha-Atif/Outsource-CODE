using backend.Models;
using Microsoft.EntityFrameworkCore;
using System.Configuration;
using System.Reflection.Emit;

namespace backend.Data
{
    public class backendDbContext : DbContext
    {
        public backendDbContext() : base()
        {

        }
        public backendDbContext(DbContextOptions<backendDbContext> options)
                  : base(options)
        {
        }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            IConfiguration configuration = new ConfigurationBuilder()
            .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
            .Build();

            optionsBuilder.UseNpgsql(configuration.GetConnectionString("backendContext"));
        }

        public DbSet<User> Users { get; set; }
        public DbSet<UserLoginRequest> UserLoginRequests { get; set; }
        public DbSet<Product> Products { get; set; }
        public DbSet<ProductSize> ProductSizes { get; set; }
        public DbSet<Order> Orders { get; set; }
        public DbSet<OrderItem> OrderItems { get; set; }
        protected override void OnModelCreating(ModelBuilder builder)
        {
            base.OnModelCreating(builder);
            builder.Entity<User>().HasKey(u => u.userID);
            builder.Entity<Product>().HasKey(u => u.productID);
            builder.Entity<ProductSize>().HasKey(u => u.productSizeID);
            builder.Entity<Order>().HasKey(u => u.orderID);
            builder.Entity<OrderItem>().HasKey(u => u.orderItemID);
            builder.Entity<UserLoginRequest>().HasKey(u => u.Id);
        }
    }
}
