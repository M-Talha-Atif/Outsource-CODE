using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace backend.Migrations
{
    /// <inheritdoc />
    public partial class renaming : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "PostalCode",
                table: "Users",
                newName: "postalCode");

            migrationBuilder.RenameColumn(
                name: "Phone",
                table: "Users",
                newName: "phone");

            migrationBuilder.RenameColumn(
                name: "Password",
                table: "Users",
                newName: "password");

            migrationBuilder.RenameColumn(
                name: "LastName",
                table: "Users",
                newName: "lastName");

            migrationBuilder.RenameColumn(
                name: "FirstName",
                table: "Users",
                newName: "firstName");

            migrationBuilder.RenameColumn(
                name: "Email",
                table: "Users",
                newName: "email");

            migrationBuilder.RenameColumn(
                name: "City",
                table: "Users",
                newName: "city");

            migrationBuilder.RenameColumn(
                name: "Address",
                table: "Users",
                newName: "address");

            migrationBuilder.RenameColumn(
                name: "UserID",
                table: "Users",
                newName: "userID");

            migrationBuilder.RenameColumn(
                name: "Password",
                table: "UserLoginRequests",
                newName: "password");

            migrationBuilder.RenameColumn(
                name: "Email",
                table: "UserLoginRequests",
                newName: "email");

            migrationBuilder.RenameColumn(
                name: "Size",
                table: "ProductSizes",
                newName: "size");

            migrationBuilder.RenameColumn(
                name: "Quantity",
                table: "ProductSizes",
                newName: "quantity");

            migrationBuilder.RenameColumn(
                name: "ProductID",
                table: "ProductSizes",
                newName: "productID");

            migrationBuilder.RenameColumn(
                name: "Price",
                table: "ProductSizes",
                newName: "price");

            migrationBuilder.RenameColumn(
                name: "ProductSizeID",
                table: "ProductSizes",
                newName: "productSizeID");

            migrationBuilder.RenameColumn(
                name: "Name",
                table: "Products",
                newName: "name");

            migrationBuilder.RenameColumn(
                name: "ImageURL",
                table: "Products",
                newName: "imageURL");

            migrationBuilder.RenameColumn(
                name: "Description",
                table: "Products",
                newName: "description");

            migrationBuilder.RenameColumn(
                name: "Brand",
                table: "Products",
                newName: "brand");

            migrationBuilder.RenameColumn(
                name: "ProductID",
                table: "Products",
                newName: "productID");

            migrationBuilder.RenameColumn(
                name: "UserID",
                table: "Orders",
                newName: "userID");

            migrationBuilder.RenameColumn(
                name: "TotalPrice",
                table: "Orders",
                newName: "totalPrice");

            migrationBuilder.RenameColumn(
                name: "Status",
                table: "Orders",
                newName: "status");

            migrationBuilder.RenameColumn(
                name: "DateTime",
                table: "Orders",
                newName: "dateTime");

            migrationBuilder.RenameColumn(
                name: "OrderID",
                table: "Orders",
                newName: "orderID");

            migrationBuilder.RenameColumn(
                name: "Quantity",
                table: "OrderItems",
                newName: "quantity");

            migrationBuilder.RenameColumn(
                name: "ProductSizeID",
                table: "OrderItems",
                newName: "productSizeID");

            migrationBuilder.RenameColumn(
                name: "OrderID",
                table: "OrderItems",
                newName: "orderID");

            migrationBuilder.RenameColumn(
                name: "OrderItemID",
                table: "OrderItems",
                newName: "orderItemID");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "postalCode",
                table: "Users",
                newName: "PostalCode");

            migrationBuilder.RenameColumn(
                name: "phone",
                table: "Users",
                newName: "Phone");

            migrationBuilder.RenameColumn(
                name: "password",
                table: "Users",
                newName: "Password");

            migrationBuilder.RenameColumn(
                name: "lastName",
                table: "Users",
                newName: "LastName");

            migrationBuilder.RenameColumn(
                name: "firstName",
                table: "Users",
                newName: "FirstName");

            migrationBuilder.RenameColumn(
                name: "email",
                table: "Users",
                newName: "Email");

            migrationBuilder.RenameColumn(
                name: "city",
                table: "Users",
                newName: "City");

            migrationBuilder.RenameColumn(
                name: "address",
                table: "Users",
                newName: "Address");

            migrationBuilder.RenameColumn(
                name: "userID",
                table: "Users",
                newName: "UserID");

            migrationBuilder.RenameColumn(
                name: "password",
                table: "UserLoginRequests",
                newName: "Password");

            migrationBuilder.RenameColumn(
                name: "email",
                table: "UserLoginRequests",
                newName: "Email");

            migrationBuilder.RenameColumn(
                name: "size",
                table: "ProductSizes",
                newName: "Size");

            migrationBuilder.RenameColumn(
                name: "quantity",
                table: "ProductSizes",
                newName: "Quantity");

            migrationBuilder.RenameColumn(
                name: "productID",
                table: "ProductSizes",
                newName: "ProductID");

            migrationBuilder.RenameColumn(
                name: "price",
                table: "ProductSizes",
                newName: "Price");

            migrationBuilder.RenameColumn(
                name: "productSizeID",
                table: "ProductSizes",
                newName: "ProductSizeID");

            migrationBuilder.RenameColumn(
                name: "name",
                table: "Products",
                newName: "Name");

            migrationBuilder.RenameColumn(
                name: "imageURL",
                table: "Products",
                newName: "ImageURL");

            migrationBuilder.RenameColumn(
                name: "description",
                table: "Products",
                newName: "Description");

            migrationBuilder.RenameColumn(
                name: "brand",
                table: "Products",
                newName: "Brand");

            migrationBuilder.RenameColumn(
                name: "productID",
                table: "Products",
                newName: "ProductID");

            migrationBuilder.RenameColumn(
                name: "userID",
                table: "Orders",
                newName: "UserID");

            migrationBuilder.RenameColumn(
                name: "totalPrice",
                table: "Orders",
                newName: "TotalPrice");

            migrationBuilder.RenameColumn(
                name: "status",
                table: "Orders",
                newName: "Status");

            migrationBuilder.RenameColumn(
                name: "dateTime",
                table: "Orders",
                newName: "DateTime");

            migrationBuilder.RenameColumn(
                name: "orderID",
                table: "Orders",
                newName: "OrderID");

            migrationBuilder.RenameColumn(
                name: "quantity",
                table: "OrderItems",
                newName: "Quantity");

            migrationBuilder.RenameColumn(
                name: "productSizeID",
                table: "OrderItems",
                newName: "ProductSizeID");

            migrationBuilder.RenameColumn(
                name: "orderID",
                table: "OrderItems",
                newName: "OrderID");

            migrationBuilder.RenameColumn(
                name: "orderItemID",
                table: "OrderItems",
                newName: "OrderItemID");
        }
    }
}
