from django.test import TestCase

# Create your tests here.
# ListCreateAPIView:
# GET: Lists all instances of a model. Retrieves a list of objects from the queryset and serializes them.
# POST: Creates a new instance of a model. Deserializes the incoming data, validates it, and creates a new object.
# RetrieveUpdateDestroyAPIView:
#
# GET: Retrieves a single instance of a model. Retrieves a specific object from the queryset and serializes it.
# PUT: Updates a single instance of a model with a full representation. Deserializes the incoming data, validates it, and updates the object with the provided data.
# PATCH: Updates a single instance of a model with partial representation. Deserializes the incoming data, validates it, and updates the object with the provided data.
# DELETE: Deletes a single instance of a model. Deletes the object from the database.
# ListAPIView:
#
# GET: Lists all instances of a model. Retrieves a list of objects from the queryset and serializes them.
# CreateAPIView:
#
# POST: Creates a new instance of a model. Deserializes the incoming data, validates it, and creates a new object.
# RetrieveAPIView:
#
# GET: Retrieves a single instance of a model. Retrieves a specific object from the queryset and serializes it.
# UpdateAPIView:
#
# PUT: Updates a single instance of a model with a full representation. Deserializes the incoming data, validates it, and updates the object with the provided data.
# PATCH: Updates a single instance of a model with partial representation. Deserializes the incoming data, validates it, and updates the object with the provided data.
# DestroyAPIView:
#
# DELETE: Deletes a single instance of a model. Deletes the object from the database

# PatchMapping in angular
# const bookId = 1; // Replace with the ID of the book you want to update
#
# const updatedData = {
#   author: 'New Author' // Provide the updated values for the fields you want to update
# };
#
# this.http.patch(`http://localhost:8000/books/${bookId}/update/`, updatedData)
#   .subscribe(response => {
#     console.log('Patch request successful', response);
#     // Handle the response or perform any additional tasks
#   }, error => {
#     console.error('Error occurred during patch request', error);
#     // Handle the error appropriately
#   });


# PatchMapping in Springboot
# import org.springframework.beans.BeanUtils;
# import org.springframework.beans.factory.annotation.Autowired;
# import org.springframework.web.bind.annotation.*;
#
# import com.example.demo.entity.Book;
# import com.example.demo.repository.BookRepository;
#
# @RestController
# @RequestMapping("/books")
# public class BookController {
#     @Autowired
#     private BookRepository bookRepository;
#
#     @PatchMapping("/{id}")
#     public Book updateBook(@PathVariable Long id, @RequestBody Book updatedBook) {
#         Book existingBook = bookRepository.findById(id)
#                 .orElseThrow(() -> new ResourceNotFoundException("Book not found with id: " + id));
#
#         BeanUtils.copyProperties(updatedBook, existingBook, "id");
#
#         return bookRepository.save(existingBook);
#     }
# }
