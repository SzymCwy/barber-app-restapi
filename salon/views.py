from rest_framework import generics
from rest_framework import permissions
from .models import Service, Visit, User
from .permissions import IsOwner, IsHairdresserOrClient
from .serializers import VisitSerializerList, VisitSerializerCreate, ServiceSerializer, VisitSerializerUpdate, \
    MyVisitSerializer, MyProfileSerializer, UserSerializerCreate, UserSerializerMin, Verify, UserSerializerUpdate


class service_list(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class service_create(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]


class service_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]


class service_detail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class visit_list(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializerList
    permission_classes = [permissions.IsAdminUser]


class visit_create(generics.CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializerCreate
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class visit_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializerUpdate
    permission_classes = [IsHairdresserOrClient]


class visit_detail(generics.RetrieveAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializerList
    permission_classes = [IsHairdresserOrClient]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerMin
    permission_classes = [permissions.IsAdminUser]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerCreate


class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerUpdate
    permission_classes = [IsOwner]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerMin
    permission_classes = [permissions.IsAdminUser]


class MyProfile(generics.ListAPIView):
    queryset = User.objects.last()
    serializer_class = MyProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


class My_Visits(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = MyVisitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == "CL":
            return Visit.objects.filter(client=self.request.user)
        else:
            return Visit.objects.filter(hairdresser=self.request.user.id)


class VerifyMail(generics.CreateAPIView):
    serializer_class = Verify
    queryset = User.objects.all()
