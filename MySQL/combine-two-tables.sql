select firstName, lastName, city, state
from Person
left join Address
on Person.personId = Address.personId;

select firstName, lastName, city, state
from Person
left join Address
using (personId);
