// Main.scala
abstract class User(
                     val id: Int,
                     var name: String,
                     var email: String,
                     val passwordHash: String) {
  def login(): Boolean
  def logout(): Unit
  def updateProfile(newName: String, newEmail: String): Unit
}

case class Customer(
                     override val id: Int,
                     override var name: String,
                     override var email: String,
                     override val passwordHash: String,
                     var shippingAddress: String,
                     var billingAddress: String
                   ) extends User(id, name, email, passwordHash) {

  private var _cart = new ShoppingCart()
  private var _orders: List[Order] = Nil

  def login(): Boolean = true // Placeholder
  def logout(): Unit = println("Logged out")
  def updateProfile(newName: String, newEmail: String): Unit = {
    name = newName
    email = newEmail
  }

  def cart: ShoppingCart = _cart
  def placeOrder(): Order = {
    val newOrder = Order(Order.generateId, this, _cart.items.map(item => OrderItem(item.product, item.quantity)))
    _orders = newOrder :: _orders
    _cart = new ShoppingCart() // Reset cart
    newOrder
  }
}

case class Admin(
                  id: Int,
                  name: String,
                  email: String,
                  passwordHash: String,
                  val accessLevel: Int
                ) extends User(id, name, email, passwordHash) {

  def login(): Boolean = true
  def logout(): Unit = println("Admin logged out")
  def updateProfile(newName: String, newEmail: String): Unit = {
    name = newName
    email = newEmail
  }

  def addProduct(product: Product): Unit = println(s"Added $product")
  def updateInventory(product: Product, newStock: Int): Unit = {
    product.stock = newStock
  }
}

case class Product(
                    val id: Int,
                    var name: String,
                    var price: Double,
                    var category: ProductCategory,
                    var stock: Int
                  )

case class ProductCategory(id: Int, name: String, description: String)

class ShoppingCart {
  private var _items: List[CartItem] = Nil
  private var _total: Double = 0.0

  def items: List[CartItem] = _items
  def total: Double = _total

  def addItem(product: Product, quantity: Int): Unit = {
    _items.find(_.product == product) match {
      case Some(item) => item.quantity += quantity
      case None => _items = CartItem(product, quantity) :: _items
    }
    calculateTotal()
  }

  def removeItem(product: Product): Unit = {
    _items = _items.filterNot(_.product == product)
    calculateTotal()
  }

  private def calculateTotal(): Unit = {
    _total = _items.map(item => item.product.price * item.quantity).sum
  }
}

case class CartItem(val product: Product, var quantity: Int)

case class Order(
                  id: Int,
                  customer: Customer,
                  items: List[OrderItem],
                  var status: String = "Processing"
                ) {
  def updateStatus(newStatus: String): Unit = status = newStatus
  def generateInvoice(): String = s"Invoice for order $id"
}

object Order {
  private var lastId = 0
  def generateId: Int = { lastId += 1; lastId }
}

case class OrderItem(product: Product, quantity: Int)

class Payment(val id: Int, val order: Order, val amount: Double, val method: String) {
  def processPayment(): Boolean = true
  def refund(): Boolean = false
}
