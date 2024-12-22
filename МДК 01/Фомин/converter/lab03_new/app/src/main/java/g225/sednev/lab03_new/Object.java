package g225.sednev.lab03_new;

import androidx.annotation.NonNull;

public class Object {
    @NonNull
    public String toString(){
        return getClass().getName() + "@" + Integer.toHexString(hashCode());
    }
}
